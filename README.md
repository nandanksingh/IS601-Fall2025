            IS601 – Python for Web API Development (Fall 2025)

This repository serves as a comprehensive portfolio of coursework for IS601 – Python for Web API Development at NJIT (Fall 2025).
It encompasses all assignments and projects, each organized into dedicated folders containing:

Source code (app/) – implementation of core functionalities

Unit tests (tests/) – rigorous validation of code correctness and reliability

Supporting configuration files – ensuring consistency, reproducibility, and maintainability

The repository is fully integrated with GitHub Actions for Continuous Integration (CI), automatically executing test pipelines with 100% code coverage enforcement.
This structure not only aligns with industry best practices in software engineering but also reflects the academic rigor of the course, preparing students for real-world development environments.

        Repository Structure:-

IS601-Fall2025/
├── .github/workflows/              # CI/CD Workflows
│   ├── assignment2-tests.yml
│   ├── assignment3-tests.yml
│   ├── assignment4-tests.yml
│   ├── assignment5-tests.yml
│   ├── assignment7-tests.yml
│   ├── ...
│   ├── assignment14-tests.yml
│   ├── midterm-project-tests.yml
│   └── final-project-tests.yml
│
├── requirements.txt                # Shared dependencies
├── README.md                       # Course-level documentation
│
├── Assignment2/
│   ├── app/
│   ├── tests/
│   └── README.md (optional for details)
├── Assignment3/
│   ├── app/
│   ├── tests/
│   └── README.md (optional)
...
├── Assignment14/
│   ├── app/
│   ├── tests/
│   └── README.md
├── Midterm-Project/
│   ├── app/
│   ├── tests/
│   └── README.md
└── Final-Project/
    ├── app/
    ├── tests/
    └── README.md
