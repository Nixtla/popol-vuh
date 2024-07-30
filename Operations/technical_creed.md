# 💙 Technical Creed

At Nixtla, we believe in crafting high-quality, reliable, and user-focused software. As our creed states, we are motivated by impact, we make money to make more software, and we do a freaking good job.
This creed outlines our guiding principles to deliver consistent excellence in our projects. 

## 🔍 We always test our code

### Tests are Important
We will test to provide a snapshot of how specific parts of our product should function. It is crucial to ensure that at least the expected output of a function or process is verified, especially for new features and bug fixes. We will test bug fixes to ensure that issues do not recur, maintaining compatibility in future developments even during internal migrations. We will always prioritize the user experience, ensuring that fixes are reliable for all future users. We will also think about our colleagues and future collaborators. 

### Types of Tests
- **Unit Tests**: We will focus on testing individual components to ensure each part functions as intended.
- **End-to-End Tests**: We will validate the entire user journey, ensuring that the product works seamlessly from start to finish before each release.

## 📝 We will document our code

We will document our work for our own understanding and that of others who will read, maintain, and use our code.

### Unitary Documentation
We will document the simplest parts of the code with clear descriptions of expected behavior, making it easier for others to understand and use.

### Project Documentation
Each project will include:
- **Setup Instructions**: Guidance on how to get started with the project.
- **Running Tests**: Instructions on running existing tests and adding new ones.
- **Contribution Guidelines**: How to contribute, including code style, commit message guidelines, and more.

### Product Documentation
We will provide comprehensive documentation of our products, detailing:
- **Usage Instructions**: How to use the product, including example workflows.
- **Feature Descriptions**: Details about the features and their expected behavior.
- **Troubleshooting**: Common issues and their resolutions.

## 📊 We will benchmark our code

We will benchmark our solutions to demonstrate efficiency and effectiveness. Every new feature, release, or product will include benchmarks to show improvements over existing solutions, whether in terms of accuracy (for models) or speed. This transparency showcases our commitment to quality and provides users with confidence in our products.

## 📚 We follow Best Practices

### Conventional Commits
We will use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) to provide a consistent way to structure commit messages, making it easier to understand the project's history. This practice improves collaboration and simplifies the process of generating release notes.

**Commit Message Structure**
- **Format**: `<type>(<scope>): <subject>`
- **Types**: Common types include `feat` for new features, `fix` for bug fixes, and `docs` for documentation changes.
- **Scope**: Optional but recommended; indicates the part of the codebase affected.
- **Subject**: A brief description of the changes.

### Pull Requests
We will ensure pull requests include a title following the Conventional Commits format: `<type>(<scope>): <subject>`, e.g., `docs: update tutorials structure`. Pull requests will also be labeled appropriately to better understand the changes in releases.

### 🔤 Naming Conventions and Code Style

#### Writing Cases
We will use consistent naming conventions across our codebase:
- **snake_case**: For variable names, function names, and filenames (e.g., `my_variable`, `process_data.py`).
- **CamelCase**: For class names and type names (e.g., `MyClass`, `DataProcessor`).

#### Directory Structure
We will follow best practices for organizing our directories:
- **src/**: Contains the main source code for the project.
- **tests/**: Contains test cases, organized similarly to the `src/` directory.
- **docs/**: Documentation files, including setup guides, usage instructions, and API documentation.
- **scripts/**: Utility scripts for setup, deployment, or data processing.
- **examples/**: Example code or notebooks demonstrating how to use the project.

### Python Best Practices
- **PEP 8**: We will adhere to PEP 8, the Python style guide, for consistency and readability.
- **Docstrings**: Every function, class, and module will have clear and descriptive docstrings.
- **Type Annotations**: We will use type annotations to clarify expected input and output types, improving code readability and maintainability.
- **Code Reviews**: We will conduct regular code reviews to ensure code quality, identify potential issues, and share knowledge among team members.


## 🚀 We ship!
- We will try to commit regularly, and ship fast.
- We prioritize getting features and improvements into the hands of users quickly.
- We embrace iterative development and continuous delivery to maintain momentum.
- We value done over perfect, understanding that feedback from real users is invaluable.
- We strive to maintain high quality and reliability in every release.
