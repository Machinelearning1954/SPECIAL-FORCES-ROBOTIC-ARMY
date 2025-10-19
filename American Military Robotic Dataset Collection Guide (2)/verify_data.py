#!/usr/bin/env python3
"""
Data Verification Script for Military Vehicle Recognition Project
Author: Brandon Patterson
Date: October 2025

This script verifies the integrity and completeness of downloaded datasets.
"""

import os
import json
from pathlib import Path
from collections import defaultdict


class DataVerifier:
    """Verifies downloaded datasets for the vehicle recognition project."""
    
    def __init__(self, base_dir=None):
        """Initialize the DataVerifier."""
        self.base_dir = Path(base_dir) if base_dir else Path.cwd()
        self.data_dir = self.base_dir / "data" / "raw"
        self.metadata_dir = self.base_dir / "data" / "metadata"
        
        self.datasets = {
            "indian_vehicle": {
                "name": "Indian Vehicle Dataset",
                "expected_min_files": 50000,
                "expected_formats": [".jpg", ".jpeg", ".png", ".xml", ".txt"]
            },
            "military_vehicles": {
                "name": "Military Vehicles Dataset",
                "expected_min_files": 1000,
                "expected_formats": [".jpg", ".jpeg", ".png", ".txt"]
            },
            "military_assets": {
                "name": "Military Assets Dataset",
                "expected_min_files": 15000,
                "expected_formats": [".jpg", ".jpeg", ".png", ".txt", ".yaml"]
            }
        }
    
    def verify_dataset(self, dataset_key):
        """Verify a single dataset."""
        dataset_info = self.datasets[dataset_key]
        dataset_path = self.data_dir / dataset_key
        
        print(f"\n{'='*70}")
        print(f"VERIFYING: {dataset_info['name']}")
        print('='*70)
        
        results = {
            "dataset": dataset_key,
            "name": dataset_info['name'],
            "exists": False,
            "file_count": 0,
            "file_types": {},
            "issues": [],
            "status": "UNKNOWN"
        }
        
        # Check if directory exists
        if not dataset_path.exists():
            results['issues'].append(f"Directory not found: {dataset_path}")
            results['status'] = "FAILED"
            print(f"✗ Directory not found: {dataset_path}")
            return results
        
        results['exists'] = True
        print(f"✓ Directory exists: {dataset_path}")
        
        # Count files by type
        file_types = defaultdict(int)
        total_files = 0
        
        for file_path in dataset_path.rglob('*'):
            if file_path.is_file():
                total_files += 1
                ext = file_path.suffix.lower()
                file_types[ext] += 1
        
        results['file_count'] = total_files
        results['file_types'] = dict(file_types)
        
        print(f"✓ Total files: {total_files:,}")
        
        # Check minimum file count
        if total_files < dataset_info['expected_min_files']:
            warning = f"File count ({total_files:,}) below expected minimum ({dataset_info['expected_min_files']:,})"
            results['issues'].append(warning)
            print(f"⚠ {warning}")
        else:
            print(f"✓ File count meets minimum requirement")
        
        # Check file formats
        print(f"\nFile types found:")
        for ext, count in sorted(file_types.items(), key=lambda x: x[1], reverse=True):
            print(f"  {ext if ext else '(no extension)'}: {count:,}")
        
        # Check for expected formats
        expected_found = any(ext in file_types for ext in dataset_info['expected_formats'])
        if not expected_found:
            issue = f"No expected file formats found: {dataset_info['expected_formats']}"
            results['issues'].append(issue)
            print(f"✗ {issue}")
        else:
            print(f"✓ Expected file formats found")
        
        # Check metadata
        metadata_file = self.metadata_dir / f"{dataset_key}_metadata.json"
        if metadata_file.exists():
            print(f"✓ Metadata file exists: {metadata_file}")
            try:
                with open(metadata_file, 'r') as f:
                    metadata = json.load(f)
                print(f"✓ Metadata is valid JSON")
                print(f"  Download date: {metadata.get('download_date', 'Unknown')}")
            except json.JSONDecodeError:
                issue = "Metadata file is corrupted"
                results['issues'].append(issue)
                print(f"✗ {issue}")
        else:
            issue = f"Metadata file not found: {metadata_file}"
            results['issues'].append(issue)
            print(f"⚠ {issue}")
        
        # Determine overall status
        if not results['issues']:
            results['status'] = "PASSED"
            print(f"\n✓ Verification PASSED")
        elif total_files > 0:
            results['status'] = "WARNING"
            print(f"\n⚠ Verification PASSED with warnings")
        else:
            results['status'] = "FAILED"
            print(f"\n✗ Verification FAILED")
        
        return results
    
    def verify_all(self):
        """Verify all datasets."""
        print("\n" + "="*70)
        print("DATA VERIFICATION REPORT")
        print("="*70)
        print(f"Base Directory: {self.base_dir}")
        print(f"Data Directory: {self.data_dir}")
        
        all_results = {}
        for dataset_key in self.datasets.keys():
            results = self.verify_dataset(dataset_key)
            all_results[dataset_key] = results
        
        # Summary
        print("\n" + "="*70)
        print("VERIFICATION SUMMARY")
        print("="*70)
        
        total_files = 0
        passed = 0
        warnings = 0
        failed = 0
        
        for dataset_key, results in all_results.items():
            status_symbol = {
                "PASSED": "✓",
                "WARNING": "⚠",
                "FAILED": "✗",
                "UNKNOWN": "?"
            }.get(results['status'], "?")
            
            print(f"{status_symbol} {results['name']}: {results['status']}")
            print(f"  Files: {results['file_count']:,}")
            
            if results['issues']:
                print(f"  Issues: {len(results['issues'])}")
                for issue in results['issues']:
                    print(f"    - {issue}")
            
            total_files += results['file_count']
            
            if results['status'] == "PASSED":
                passed += 1
            elif results['status'] == "WARNING":
                warnings += 1
            elif results['status'] == "FAILED":
                failed += 1
        
        print(f"\nTotal Datasets: {len(all_results)}")
        print(f"Passed: {passed}")
        print(f"Warnings: {warnings}")
        print(f"Failed: {failed}")
        print(f"Total Files: {total_files:,}")
        
        # Overall status
        if failed > 0:
            print(f"\n✗ Overall Status: FAILED")
            return False
        elif warnings > 0:
            print(f"\n⚠ Overall Status: PASSED with warnings")
            return True
        else:
            print(f"\n✓ Overall Status: ALL CHECKS PASSED")
            return True


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Verify downloaded datasets for Military Vehicle Recognition Project"
    )
    parser.add_argument(
        '--dataset',
        choices=['indian_vehicle', 'military_vehicles', 'military_assets', 'all'],
        default='all',
        help='Specify which dataset to verify (default: all)'
    )
    parser.add_argument(
        '--base-dir',
        type=str,
        default=None,
        help='Base directory for data storage (default: current directory)'
    )
    
    args = parser.parse_args()
    
    # Initialize verifier
    verifier = DataVerifier(base_dir=args.base_dir)
    
    # Verify datasets
    if args.dataset == 'all':
        success = verifier.verify_all()
    else:
        results = verifier.verify_dataset(args.dataset)
        success = results['status'] in ["PASSED", "WARNING"]
    
    # Exit with appropriate code
    exit(0 if success else 1)


if __name__ == "__main__":
    main()

