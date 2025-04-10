# MrFuGenerativeAI

This repository provides a suite of tools for inferencing and training **Stable Diffusion v1.5** models, developed as part of the NTUT AC03519 project **"Generative AI Technology and Applications."**

## Cuation!
This repository is a reference for education only. It is not actively supported.

## Overview

This repo includes the following components:

1. **Diffusion Model**  
   A customized Gradio WebUI for running Stable Diffusion v1.5 on Google Colab or a local machine.

2. **Textual Inversion**  
   A simple WebUI for training Stable Diffusion v1.5 Textual Inversion models on Google Colab or a local machine.

3. **Dreambooth**  
   A user-friendly WebUI for training Stable Diffusion v1.5 Dreambooth models on Google Colab.  
   **Note:** This module requires significant VRAM. For best performance, it is recommended to run Dreambooth on a local machine.

4. **LoRA**  
   A streamlined WebUI for training Stable Diffusion v1.5 LoRA models on Google Colab or a local machine. The generated `<pytorch_lora_weights_kohya.safetensors>` file is compatible with the A1111 WebUI LoRA model.

## Getting Started

### Prerequisites

- [Git](https://git-scm.com/)
- Python 3.10+
- [Pytorch on CUDA 12.4](https://pytorch.org/)
- [Google Colab](https://colab.research.google.com/) (if you choose to run notebooks in the cloud)
- Local machine setup (if running locally, ensure you have sufficient VRAM for Dreambooth)


### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/MrFuGenerativeAI.git
   cd MrFuGenerativeAI

2. Setup the Environment: In each Jupyter notebook, run the 1st cell to install required python packages.

3. Running the WebUI: For Google Colab, open the corresponding notebook github address and follow the in-notebook instructions.

For local setups, run the provided scripts in VSCode with Jupyter plugin installed to launch the Gradio WebUI.

# Usage
1. Diffusion Model: Run `<MrFu_Stable_Diffusion_WebUI.ipynb>` to lauch Gradio WebUI and start inferencing using Stable Diffusion v1.5.

2. Textual Inversion: Run `<MrFu_Textual_Inversion.ipynb>` to train your custom Textual Inversion model via the provided WebUI.

3. Dreambooth: Run `<MrFu_Dreambooth.ipynb>`to initiate Dreambooth training using the Colab notebook or local setup, keeping in mind the VRAM requirements.

4. LoRA: Run `<MrFu_LoRA.ipynb>` to train a LoRA model and generate <pytorch_lora_weights_kohya.safetensors> compatible with A1111 WebUI.

For more detailed instructions, please refer to the individual module documentation within this repository.

# Contributing
Contributions are welcome! If you would like to improve the repository or fix any issues, please fork the repository, make your changes, and submit a pull request.

# License
This project is licensed under the MIT License. 

# Acknowledgments
- NTUT AC03519 "Generative AI Technology and Applications" – for the support and inspiration behind this project.

- The Huggingface and Stable Diffusion staff and community for their contributions and insights.