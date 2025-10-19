# GitHub Repository Structure - Military Vehicle Recognition Capstone

## Complete Repository Organization

```
military-vehicle-recognition-capstone/
│
├── README.md                                    # Main project documentation (START HERE)
├── LICENSE                                      # MIT License
├── .gitignore                                   # Git ignore rules
├── requirements.txt                             # Top-level Python dependencies
│
├── docs/                                        # Additional documentation
│   ├── PROJECT_PROPOSAL.md                      # Step 3: Project proposal
│   ├── FINAL_REPORT.md                          # Final project report
│   └── API_REFERENCE.md                         # API documentation
│
├── step2-data-collection/                       # STEP 2: Data Collection
│   ├── README.md                                # Data collection overview
│   ├── DATASETS.md                              # Detailed dataset information
│   │
│   ├── scripts/                                 # Data collection scripts
│   │   ├── download_datasets.sh                 # Kaggle download script
│   │   ├── data_collection.py                   # Python automation script
│   │   └── verify_data.py                       # Data verification
│   │
│   ├── notebooks/                               # Jupyter notebooks
│   │   └── 01_data_collection.ipynb             # Data collection notebook
│   │
│   ├── data/                                    # Data directory
│   │   ├── README.md                            # Data organization guide
│   │   ├── raw/                                 # Raw downloaded data
│   │   │   ├── indian_vehicle_dataset/
│   │   │   ├── military_vehicles/
│   │   │   └── military_assets/
│   │   └── metadata/                            # Dataset metadata
│   │       ├── data_sources.csv
│   │       └── dataset_statistics.json
│   │
│   └── reports/                                 # Data collection reports
│       └── data_collection_report.md
│
├── step3-project-proposal/                      # STEP 3: Project Proposal (Optional)
│   ├── PROJECT_PROPOSAL.md                      # Formal project proposal
│   ├── problem_statement.md                     # Problem definition
│   └── success_criteria.md                      # Success metrics
│
├── step4-research-survey/                       # STEP 4: Survey Existing Research
│   ├── README.md                                # Research survey overview
│   ├── RESEARCH_SURVEY.md                       # Comprehensive research analysis
│   ├── STEP4_SUMMARY.md                         # Completion summary
│   │
│   ├── papers/                                  # Research papers (PDFs)
│   │   ├── yolov8_paper.pdf
│   │   ├── vehicle_detection_survey.pdf
│   │   └── papers_list.md                       # Annotated bibliography
│   │
│   ├── analysis/                                # Research analysis
│   │   ├── baseline_metrics.md                  # Performance baselines
│   │   ├── repository_analysis.md               # Code repository analysis
│   │   ├── comparative_analysis.md              # Method comparisons
│   │   └── lessons_learned.md                   # Key insights
│   │
│   ├── reproduced-solutions/                    # Reproduced experiments
│   │   ├── baseline_reproduction.ipynb          # Reproduced results
│   │   ├── yolov8_baseline/                     # YOLOv8 reproduction
│   │   └── detectron2_baseline/                 # Detectron2 reproduction
│   │
│   └── presentations/                           # Presentation materials
│       └── research-survey-presentation/        # 12-slide presentation
│           ├── slide_state.json                 # Presentation metadata
│           ├── title_slide.html
│           ├── introduction.html
│           ├── research_landscape.html
│           ├── key_papers.html
│           ├── baseline_metrics.html
│           ├── comparative_analysis.html
│           ├── lessons_learned.html
│           ├── proposed_enhancements.html
│           ├── performance_targets.html
│           └── conclusion.html
│
├── step5-data-wrangling/                        # STEP 5: Data Wrangling
│   ├── README.md                                # Data wrangling overview
│   ├── STEP5_SUMMARY.md                         # Completion summary
│   │
│   ├── notebooks/                               # Jupyter notebooks
│   │   ├── 01_data_wrangling_and_cleaning.ipynb # Main wrangling notebook
│   │   ├── 02_exploratory_data_analysis.ipynb   # EDA notebook
│   │   └── 03_data_export.ipynb                 # Export notebook
│   │
│   ├── scripts/                                 # Data processing scripts
│   │   ├── clean_data.py                        # Data cleaning
│   │   ├── handle_missing_values.py             # Missing value handling
│   │   ├── detect_outliers.py                   # Outlier detection
│   │   └── export_formats.py                    # Multi-format export
│   │
│   ├── data/                                    # Processed data
│   │   ├── processed/                           # Cleaned datasets
│   │   │   ├── cleaned_dataset.csv              # CSV format
│   │   │   ├── cleaned_dataset.parquet          # Parquet format
│   │   │   ├── yolo_format/                     # YOLO labels
│   │   │   ├── coco_format/                     # COCO JSON
│   │   │   └── pascal_voc_format/               # Pascal VOC XML
│   │   └── splits/                              # Train/val/test splits
│   │       ├── train.csv
│   │       ├── val.csv
│   │       └── test.csv
│   │
│   ├── visualizations/                          # EDA visualizations
│   │   ├── 01_data_source_distribution.png
│   │   ├── 02_vehicle_class_distribution.png
│   │   ├── 03_image_dimensions_distribution.png
│   │   ├── 04_aspect_ratio_distribution.png
│   │   ├── 05_bbox_size_distribution.png
│   │   ├── 06_missing_values_heatmap.png
│   │   ├── 07_class_imbalance_chart.png
│   │   ├── 08_outlier_detection_boxplot.png
│   │   ├── 09_correlation_matrix.png
│   │   └── 10_source_class_heatmap.png
│   │
│   └── reports/                                 # Analysis reports
│       ├── DATA_WRANGLING_REPORT.md             # Comprehensive report
│       ├── data_quality_assessment.md           # Quality metrics
│       └── cleaning_decisions.md                # Cleaning rationale
│
├── step6-benchmark-model/                       # STEP 6: Benchmark Your Model (Optional)
│   ├── README.md                                # Benchmarking overview
│   ├── notebooks/
│   │   └── baseline_model.ipynb                 # Baseline model
│   └── results/
│       └── baseline_results.json                # Baseline metrics
│
├── step7-experiment-models/                     # STEP 7: Experiment with Various Models
│   ├── README.md                                # Experimentation overview
│   │
│   ├── notebooks/                               # Experiment notebooks
│   │   ├── 01_yolov8_experiments.ipynb          # YOLOv8 experiments
│   │   ├── 02_yolov5_comparison.ipynb           # YOLOv5 comparison
│   │   ├── 03_faster_rcnn_experiments.ipynb     # Faster R-CNN
│   │   └── 04_model_comparison.ipynb            # Final comparison
│   │
│   ├── configs/                                 # Model configurations
│   │   ├── yolov8_config.yaml
│   │   ├── yolov5_config.yaml
│   │   └── faster_rcnn_config.py
│   │
│   ├── results/                                 # Experiment results
│   │   ├── yolov8_results.json
│   │   ├── yolov5_results.json
│   │   ├── faster_rcnn_results.json
│   │   └── comparison_table.csv
│   │
│   └── reports/
│       └── model_selection_report.md            # Model selection rationale
│
├── step8-scale-prototype/                       # STEP 8: Scale Your Prototype
│   ├── README.md                                # Scaling overview
│   ├── notebooks/
│   │   └── scaling_experiments.ipynb            # Scaling tests
│   └── reports/
│       └── scaling_analysis.md                  # Scaling results
│
├── step9-deployment-method/                     # STEP 9: Pick Your Deployment Method
│   ├── README.md                                # Deployment method overview
│   ├── deployment_comparison.md                 # Platform comparison
│   └── deployment_decision.md                   # Final decision
│
├── step10-deployment-design/                    # STEP 10: Design Your Deployment Solution
│   ├── README.md                                # Design overview
│   ├── architecture_diagram.png                 # System architecture
│   ├── deployment_architecture.md               # Architecture document
│   └── infrastructure_plan.md                   # Infrastructure planning
│
├── step11-deployment-implementation/            # STEP 11: Deployment Implementation
│   ├── README.md                                # Implementation overview
│   ├── deployment_log.md                        # Deployment steps
│   └── testing_results.md                       # Deployment testing
│
├── step12-share-project/                        # STEP 12: Share Your Project
│   ├── README.md                                # Sharing overview
│   ├── blog_post.md                             # Blog post draft
│   ├── presentation.pdf                         # Final presentation
│   └── demo_video_script.md                     # Demo script
│
├── models/                                      # ML Models
│   ├── README.md                                # Models documentation
│   │
│   ├── training/                                # Training scripts
│   │   ├── train_yolov8.py                      # YOLOv8 training
│   │   ├── train_config.yaml                    # Training configuration
│   │   └── training_utils.py                    # Training utilities
│   │
│   ├── weights/                                 # Model weights
│   │   ├── best.pt                              # Best model checkpoint
│   │   ├── last.pt                              # Last checkpoint
│   │   └── yolov8m_pretrained.pt                # Pretrained weights
│   │
│   ├── configs/                                 # Model configurations
│   │   └── dataset.yaml                         # Dataset config for YOLO
│   │
│   └── evaluation/                              # Model evaluation
│       ├── evaluate_model.py                    # Evaluation script
│       └── evaluation_results.json              # Metrics
│
├── webapp/                                      # WEB APPLICATION (Phase 2)
│   ├── README.md                                # Application documentation
│   ├── DEPLOYMENT_GUIDE.md                      # Deployment instructions
│   ├── requirements.txt                         # Python dependencies
│   │
│   ├── backend_api/                             # Flask Backend
│   │   ├── README.md                            # Backend documentation
│   │   ├── requirements.txt                     # Backend dependencies
│   │   │
│   │   ├── src/                                 # Source code
│   │   │   ├── __init__.py
│   │   │   ├── main.py                          # Application entry point
│   │   │   │
│   │   │   ├── routes/                          # API routes
│   │   │   │   ├── __init__.py
│   │   │   │   ├── detection.py                 # Vehicle detection API
│   │   │   │   └── user.py                      # User management API
│   │   │   │
│   │   │   ├── models/                          # Database models
│   │   │   │   ├── __init__.py
│   │   │   │   └── user.py                      # User model
│   │   │   │
│   │   │   ├── utils/                           # Utility functions
│   │   │   │   ├── __init__.py
│   │   │   │   ├── image_processing.py          # Image utilities
│   │   │   │   └── model_loader.py              # Model loading
│   │   │   │
│   │   │   ├── static/                          # Frontend files
│   │   │   │   ├── index.html                   # Main UI
│   │   │   │   ├── css/
│   │   │   │   │   └── styles.css               # Custom styles
│   │   │   │   ├── js/
│   │   │   │   │   └── app.js                   # Frontend logic
│   │   │   │   └── images/
│   │   │   │       └── logo.png                 # Logo
│   │   │   │
│   │   │   └── database/                        # Database
│   │   │       └── app.db                       # SQLite database
│   │   │
│   │   ├── tests/                               # Unit tests
│   │   │   ├── __init__.py
│   │   │   ├── test_api.py                      # API tests
│   │   │   └── test_detection.py                # Detection tests
│   │   │
│   │   ├── logs/                                # Application logs
│   │   │   └── app.log
│   │   │
│   │   ├── config/                              # Configuration files
│   │   │   ├── development.py                   # Dev config
│   │   │   ├── production.py                    # Prod config
│   │   │   └── config.py                        # Base config
│   │   │
│   │   ├── Dockerfile                           # Docker configuration
│   │   ├── docker-compose.yml                   # Docker Compose
│   │   ├── .env.example                         # Environment variables
│   │   └── wsgi.py                              # WSGI entry point
│   │
│   ├── frontend/                                # Frontend (if separate)
│   │   ├── README.md
│   │   ├── package.json
│   │   └── src/
│   │
│   └── deployment/                              # Deployment files
│       ├── aws/
│       │   ├── cloudformation.yaml              # AWS CloudFormation
│       │   └── deploy_aws.sh                    # AWS deployment script
│       ├── gcp/
│       │   └── deploy_gcp.sh                    # GCP deployment script
│       ├── azure/
│       │   └── deploy_azure.sh                  # Azure deployment script
│       ├── docker/
│       │   ├── Dockerfile
│       │   └── docker-compose.yml
│       └── kubernetes/
│           ├── deployment.yaml
│           └── service.yaml
│
├── tests/                                       # Project-wide tests
│   ├── __init__.py
│   ├── test_data_processing.py                  # Data tests
│   ├── test_model.py                            # Model tests
│   └── test_integration.py                      # Integration tests
│
├── scripts/                                     # Utility scripts
│   ├── setup_environment.sh                     # Environment setup
│   ├── download_models.sh                       # Model download
│   ├── run_tests.sh                             # Test runner
│   └── deploy.sh                                # Deployment script
│
├── notebooks/                                   # Additional notebooks
│   ├── exploratory_analysis.ipynb               # General EDA
│   ├── model_evaluation.ipynb                   # Model evaluation
│   └── results_visualization.ipynb              # Results viz
│
├── data/                                        # Data directory (if not in steps)
│   ├── .gitkeep                                 # Keep directory in git
│   └── README.md                                # Data organization
│
├── logs/                                        # Project logs
│   └── .gitkeep
│
├── outputs/                                     # Model outputs
│   ├── predictions/                             # Prediction results
│   └── visualizations/                          # Output visualizations
│
└── .github/                                     # GitHub specific files
    ├── workflows/                               # GitHub Actions
    │   ├── ci.yml                               # Continuous Integration
    │   └── deploy.yml                           # Deployment workflow
    └── ISSUE_TEMPLATE/
        ├── bug_report.md                        # Bug report template
        └── feature_request.md                   # Feature request template
```

---

## Key Files Description

### Root Level Files

| File | Purpose |
|------|---------|
| `README.md` | Main project documentation with executive summary, instructions, and file guide |
| `LICENSE` | MIT License for the project |
| `.gitignore` | Specifies files to ignore in Git (venv, __pycache__, .env, etc.) |
| `requirements.txt` | Top-level Python dependencies for the entire project |

### Phase 1 Submissions (Steps 2, 4, 5)

| Directory | Contents | Key Files |
|-----------|----------|-----------|
| `step2-data-collection/` | Data collection scripts, datasets, documentation | `DATASETS.md`, `download_datasets.sh`, `data_collection.py` |
| `step4-research-survey/` | Research analysis, baselines, presentation | `RESEARCH_SURVEY.md`, `baseline_metrics.md`, presentation slides |
| `step5-data-wrangling/` | Data cleaning, visualizations, processed data | `DATA_WRANGLING_REPORT.md`, wrangling notebook, 10 visualizations |

### Phase 2 Deployment (webapp/)

| Directory | Contents | Key Files |
|-----------|----------|-----------|
| `webapp/backend_api/` | Flask application with API and frontend | `main.py`, `detection.py`, `index.html` |
| `webapp/backend_api/src/routes/` | API endpoints | `detection.py` (vehicle detection API) |
| `webapp/backend_api/src/static/` | Frontend UI | `index.html` (professional web interface) |
| `models/` | Trained models and training scripts | `best.pt`, `train_yolov8.py` |

### Documentation Files

| File | Purpose |
|------|---------|
| `webapp/README.md` | Application documentation and API reference |
| `webapp/DEPLOYMENT_GUIDE.md` | Step-by-step deployment instructions for 5 platforms |
| `step4-research-survey/RESEARCH_SURVEY.md` | Comprehensive research analysis of 15 papers |
| `step5-data-wrangling/reports/DATA_WRANGLING_REPORT.md` | Data cleaning and wrangling analysis |

---

## File Naming Conventions

### Python Files
- **Scripts**: `snake_case.py` (e.g., `data_collection.py`)
- **Modules**: `snake_case.py` (e.g., `image_processing.py`)
- **Classes**: PascalCase in code (e.g., `class VehicleDetector`)

### Notebooks
- **Numbered**: `01_descriptive_name.ipynb`
- **Sequential**: Follow logical order of execution

### Documentation
- **All caps**: `README.md`, `LICENSE`, `DATASETS.md`
- **Descriptive**: `data_wrangling_report.md`, `deployment_guide.md`

### Data Files
- **CSV**: `lowercase_with_underscores.csv`
- **JSON**: `lowercase_with_underscores.json`
- **Models**: `best.pt`, `last.pt`, `model_v1.pt`

---

## Git Best Practices

### .gitignore Contents
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Data (large files)
*.csv
*.parquet
data/raw/
data/processed/

# Models (use Git LFS)
*.pt
*.pth
*.h5
*.pkl

# Environment
.env
.env.local

# Logs
logs/
*.log

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
```

### Git LFS for Large Files
```bash
# Track large model files
git lfs track "*.pt"
git lfs track "*.pth"
git lfs track "*.h5"

# Track large datasets
git lfs track "*.parquet"
```

---

## Repository Size Management

### Large Files Strategy
1. **Models**: Use Git LFS or cloud storage (S3, GCS)
2. **Datasets**: Provide download scripts instead of committing data
3. **Visualizations**: Commit PNG/JPG (compressed)
4. **Videos**: Link to external hosting (YouTube, Vimeo)

### Recommended Sizes
- **Total repo**: < 1GB (without LFS)
- **Individual files**: < 100MB
- **Use LFS for**: Files > 50MB

---

## Professional Portfolio Standards

### Must-Have Elements
✅ Clear README with executive summary  
✅ Well-organized folder structure  
✅ Comprehensive documentation  
✅ Clean, commented code  
✅ All intermediate submissions  
✅ Deployed application with instructions  
✅ Professional presentation materials  

### Nice-to-Have Elements
⭐ CI/CD workflows (GitHub Actions)  
⭐ Unit tests with coverage  
⭐ Docker containerization  
⭐ API documentation (Swagger/OpenAPI)  
⭐ Blog post or technical writeup  
⭐ Demo video  

---

## Quick Navigation Guide

**For Reviewers:**
1. Start with `README.md` (executive summary)
2. Review `step2-data-collection/DATASETS.md` (data sources)
3. Check `step4-research-survey/RESEARCH_SURVEY.md` (research)
4. Examine `step5-data-wrangling/reports/DATA_WRANGLING_REPORT.md` (data quality)
5. Test application: `webapp/README.md` (deployment instructions)

**For Users:**
1. Read `README.md` (overview)
2. Follow `webapp/README.md` (how to use)
3. Deploy using `webapp/DEPLOYMENT_GUIDE.md`

**For Developers:**
1. Clone repository
2. Follow `README.md` installation instructions
3. Review `webapp/backend_api/src/` (source code)
4. Check `models/training/` (training scripts)

---

This structure ensures:
- ✅ **Rubric Compliance**: All required deliverables organized
- ✅ **Professional Quality**: Industry-standard organization
- ✅ **Easy Navigation**: Clear hierarchy and naming
- ✅ **Scalability**: Room for future additions
- ✅ **Portfolio Ready**: Impressive to hiring managers

