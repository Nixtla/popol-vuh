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

#### Reviews

1. **We Respond Promptly and Communicate Clearly**  
   We review PRs in a timely manner and communicate our availability, valuing our teammates' time and efforts.

2. **We Begin with Positivity**  
   We start each review by acknowledging the contributor's efforts and highlighting what they did well, fostering a supportive environment.

3. **We Provide Constructive and Specific Feedback**  
   We offer clear, actionable feedback, explaining our reasoning to promote understanding and continuous learning.

4. **We Focus on Code, Not the Person**  
   We critique the code objectively, using respectful and inclusive language, ensuring our feedback is about the work, not the individual.

5. **We Balance Thoroughness with Respect for Time**  
   We prioritize critical issues and recognize when a solution is sufficient, avoiding unnecessary delays and perfectionism.

6. **We Encourage Learning and Collaboration**  
   We suggest resources, offer to discuss challenges, and foster open dialogue, promoting a culture of shared learning and teamwork.

7. **We Are Mindful of Our Tone**  
   We use friendly and supportive language, avoiding abrupt phrases, and being conscious of how our words may be perceived.

8. **We Follow Up and Close the Loop**  
   We acknowledge changes made by contributors, providing continued support until the PR is ready, and celebrating the final approval.

9. **We Respect Diversity in Experience and Perspective**  
   We mentor less experienced developers and embrace diverse approaches, recognizing that different perspectives strengthen our team.

We commit to these principles to create a positive, constructive, and collaborative environment for everyone involved in the code review process.

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
- **[PEP 8](https://peps.python.org/pep-0008/)**: We will adhere to PEP 8, the Python style guide, for consistency and readability.
- **Docstrings**: Every function, class, and module will have clear and descriptive docstrings.
- **Type Annotations**: We will use type annotations to clarify expected input and output types, improving code readability and maintainability.
- **Code Reviews**: We will conduct regular code reviews to ensure code quality, identify potential issues, and share knowledge among team members.

### Web Best Practices
On our web products, we focus on 2 priorities when we write code:
- **Developer Velocity.** We understand all code is a liability, and the velocity of developers to change a codebase is inversely proportional to the size of the codebase and the team. We actively try to lessen this effect.
- **Correctness.** The purpose of code is to do what it’s supposed to do in the way it’s supposed to do it.

For the purpose of each of these two priorities, we have made a number of decisions for our codebase:

#### Strict and clear typing. 
We aim to be as type-safe as possible. Types are not only built-in tests, but also built-in documentation, linking together our codebase to be a cohesive whole in a way computers can understand and humans can read. We understand:
- Types allow us to write more correct code with less effort, since instead finding bugs, we allow the type-checker to find them for us
- Types allow us to move more quickly in the long-term, by leading to a codebase that can more easily be understood, changed and refactored without fear of breaking

#### Style
We consider things that don’t alter the execution of code to be “style”. We aim to keep it consistent and delegate these tasks and decisions to automatic tools as much as possible, in an effort to maintain developer velocity by reducing the time we have to spend thinking about this.
- **Prettier.** Whatever prettier outputs is the correct style. 
- **ESLint.** Whatever ESLint is configured to warn about, is wrong style.
- **We use camelCase**, trailing commas, and semicolons.
We are flexible to changes to our style, as long was we can ensure consistency and it helps us achieve our velocity and correctness goals.

#### Maleable code
Our codebase is very dynamic and our company young and experimenting. Most lines of code we write might not exist as written in a few months time
- Writing code that’s easily findable and replaceable. Verbosity is not our enemy but our friend. The less we can overload a word, term or token, the better.
- There’s many ways to put the same pixels on the screen. We err for the simplest that best solves the problem


## 🚀 We ship!
- We will try to commit regularly, and ship fast.
- We prioritize getting features and improvements into the hands of users quickly.
- We embrace iterative development and continuous delivery to maintain momentum.
- We value done over perfect, understanding that feedback from real users is invaluable.
- We strive to maintain high quality and reliability in every release.
