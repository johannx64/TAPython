# Chameleon Tools

## Overview
Chameleon Tools is a suite of Python-based tools designed for Unreal Engine, providing functionalities for asset management, UI manipulation, and more. The tools leverage Unreal's Python API to enhance the development workflow.

## Features
- **ChameleonSketch**: A tool for sketching and manipulating assets within the Unreal Engine environment.
- **MaskingTool**: A tool for creating and managing masks for various assets.
- **ChameleonGallery**: A gallery tool for displaying and managing various assets and their properties.
- **Shelf**: A customizable shelf for quick access to frequently used tools and assets.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd ChameleonTools
   ```
3. Ensure that you have Unreal Engine installed and configured to use Python scripting.

## Usage
### ChameleonSketch
- Initialize with a JSON path:
  ```python
  sketch = ChameleonSketch(jsonPath)
  ```
- Call methods like `on_demo_button_click()` to interact with the tool.

### MaskingTool
- Initialize with a JSON path:
  ```python
  masking_tool = MaskingTool(jsonPath)
  ```
- Use methods like `add_mask_object()` to add mask objects to the scene.

### ChameleonGallery
- Initialize with a JSON path:
  ```python
  gallery = ChameleonGallery(jsonPath)
  ```
- Use methods like `launch_other_galleries()` to open additional galleries.

### Shelf
- Initialize with a JSON path:
  ```python
  shelf = Shelf(jsonPath)
  ```
- Use methods like `add_py_code_shortcut()` to add shortcuts to the shelf.

## Dependencies
- Unreal Engine (version X.X or higher)
- Python (version X.X or higher)

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Unreal Engine for providing a powerful game development platform.
- The Python community for their contributions to the language and its libraries.
