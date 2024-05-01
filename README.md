<img src="https://raw.githubusercontent.com/liamarguedas/Commitify/master/img/logo_header.png" alt="Commitify logo"/>

> Commitify is a user-friendly tool designed to simplify the process of making commits on GitHub.

![GitHub release (latest by date)](https://img.shields.io/badge/release-v1.0.0-green)
![language (python)](https://img.shields.io/badge/language-python-blue)
![language (Bash)](https://img.shields.io/badge/language-Bash-green)
![license](https://img.shields.io/badge/license-GPL--3.0-yellow)

#### What is a Commitify?

Commitify is a user-friendly tool designed to simplify the process of making commits on GitHub, helping developers maintain a consistent and active presence on their repositories. With Commitify, you can effortlessly manage your commit history, ensuring that your GitHub profile reflects your ongoing contributions and dedication to your projects.
___

## Key Features
- **Fake Commit Generation**: Automatically generates fake commits on GitHub repositories.
- **Configurable Commit Frequency**: Allows users to specify the number of random commits to be made per day, providing flexibility in demonstrating activity levels.
- **User-Friendly Interface**: Simplified operation with a one-time setup process. Users need only to run the tool once, configure it, and it will run in the background every time the user's computer starts.
- **Consistency in Contributions**: Aids developers in maintaining a consistent appearance of activity within GitHub's contribution statistics.
- **Customization Options**:
    - **File Type Selection**: Enables users to choose the type of files to include in the fake commits, ensuring they align with the user's preferred language or project.
    - **Custom Comments**: Allows users to set custom comments for the fake commits, providing a personalized touch to the generated activity.
    - **Repository Selection**: Permits users to specify the repository where the fake commits will be applied, granting control over the visibility and context of the activity.
- **Automated Execution**: Runs seamlessly in the background, requiring minimal user intervention once configured.
- **Compatibility**: Compatible with various operating systems, ensuring accessibility to a wide range of developers.
- **Open Source**: Encourages community involvement and transparency by being open-source, allowing developers to contribute to its improvement and customization.

## Get Started

To begin using Commitify, follow these steps:

1. **Create a GitHub Repository**:
   - Start by creating a new repository on GitHub. You can name it as you wish, but ensure it remains empty. Do not add any files, including `LICENSE` or `README.md`.

2. **Clone Commitify**:
   - Open your terminal and navigate to the directory where you want to store Commitify.
   - Run the following commands:
     ```bash
     mkdir Commitify
     cd Commitify
     git clone https://github.com/liamarguedas/Commitify.git
     ```

3. **Install Dependencies**:
   - Once the repository is cloned, execute the `build.py` script with Python:
     ```bash
     python build.py
     ```
   - This script will automatically install all the necessary dependencies for Commitify in your environment, if they are not already installed.

4. **Configuration**:
   - Upon running `build.py`, the CLI will prompt you for repository information and Commitify configuration.
   - You can set your own configuration or leave it blank to use the default settings.
     - **Repository URL**: Provide the URL of the GitHub repository you created earlier.
     - **Branch**: Specify the branch of the repository. If left blank, "master" will be used.
     - **Commits**: Enter the number of commits Commitify will execute daily. Leaving this blank will result in a random number of commits each day.
     - **File**: Choose the file type to be added to the repository. Specify only the extension (e.g., `py`, `js`, `rs`) without the dot. If left blank, Python files (`py`) will be used by default.
     
     *Note: Providing the repository URL is mandatory.*

5. **Ready to Use**:
   - After configuring Commitify, it will be ready for use.
   - A folder named `Commitify` will be created in the root directory, linked to your GitHub repository, where all commits will occur.
   - Additionally, a script will be generated to run automatically upon computer startup. You can also manually execute it whenever necessary from the startup folder.

With these steps completed, Commitify is set up and ready to demonstrate consistent activity on your GitHub repository.

## Platform Compatibility

- **Windows**: Fully supported and ready to use.
- **Linux**: Currently at around 90% completion.
- **macOS**: Currently at around 60% completion.

## Donations

Commitify is a freely available, open-source CLI Tool crafted during my limited free time. If you find value in the project and wish to contribute to its ongoing development, kindly consider making a small donation. Your support is genuinely appreciated!

[Donate with PayPal](https://www.paypal.me/ILIAMFTW)

## Contributors

<a href="https://github.com/liamarguedas/Commitify/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=liamarguedas/Commitify" />
</a>

## License

Commitify was created by [Liam Arguedas](https://github.com/liamarguedas)
and is licensed under the [GPL-3.0 license](/LICENSE).
