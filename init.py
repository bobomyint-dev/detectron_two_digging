"""
This script performs object detection using the Detectron2 library.
The script mainly used for the following links:
    https://medium.com/@hirotoschwert/digging-into-detectron-2-47b2e794fabd
    https://medium.com/@hirotoschwert/digging-into-detectron-2-part-2-dd6e8b0526e
    https://medium.com/@hirotoschwert/digging-into-detectron-2-part-3-1ecc27efc0b2
    https://medium.com/@hirotoschwert/digging-into-detectron-2-part-4-3d1436f91266
    https://medium.com/@hirotoschwert/digging-into-detectron-2-part-5-6e220d762f9

The github repository for the Detectron2 library can be found at:
    https://github.com/facebookresearch/detectron2?tab=readme-ov-file


Functions:
    setup_cfg(config_file, weights_file, score_thresh, device) -> CfgNode:
        Sets up the configuration for the Detectron2 model.
        
    get_predictor(cfg: CfgNode) -> DefaultPredictor:
        Creates a predictor object using the given configuration.
        
    perform_inference(predictor: DefaultPredictor, image_path: str) -> dict:
        Performs inference on the given image and returns the predictions.
        
    visualize_predictions(image_path: str, predictions: dict, metadata: MetadataCatalog) -> None:
        Visualizes the predictions on the image and displays it.
        
    main(config_file: str, weights_file: str, image_path: str, score_thresh: float, device: str) -> None:
        Main function to set up the configuration, perform inference, and visualize predictions.
        
Args:
    config_file (str): Path to the configuration file.
    weights_file (str): Path to the model weights file.
    score_thresh (float): Score threshold for filtering predictions.
    device (str): Device to run the model on ('cpu' or 'cuda').
    image_path (str): Path to the input image.

Returns:
    None
"""

# # !python -m pip install pyyaml==5.1
# import sys, os, distutils.core
# # Note: This is a faster way to install detectron2 in Colab, but it does not include all functionalities (e.g. compiled operators).
# # See https://detectron2.readthedocs.io/tutorials/install.html for full installation instructions
# !git clone 'https://github.com/facebookresearch/detectron2'
# dist = distutils.core.run_setup("./detectron2/setup.py")
# !python -m pip install {' '.join([f"'{x}'" for x in dist.install_requires])}
# sys.path.insert(0, os.path.abspath('./detectron2'))

# # Properly install detectron2. (Please do not install twice in both ways)
# # !python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'