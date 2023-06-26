class MACRO: 

    """
    This file contains macro definitions of the project. 
    You can control the training process, configurations, 
    and virtually every aspect of the project from this file. 
    """
    #Turn off the non maximum noise supression
    
    
    # number of itterations the model will spend training 
    # can be set to 0 if you want to use predefined model and process the images
    EPOC = 10
    
    DEVICE = 0            # gpu device
    BATCH_SIZE = 128        # batch size used for training    
    NUM_WORKERS = 1        # workers for gpu. 
    NMS_THRESHOLD = 0.10    # Non Maximum Noise Supression Union Threshold

    WINDOW_SIZE = 55    # Windows size used during training

    TRAIN_RANGE = range(0, 15)         #Files that are used for training
    VALIDATION_RANGE = range(16, 21)    #Files that are used for validation
    TEST_RANGE = range(21, 31)           #Files that are used for testing

    MODELPATH = "models/Imbalanced"     #Location where the project will save a model
    BESTMODELPATH = "models/Best"       #Location where the project will save the best model
    DEFAULT_PROBABILITY = 0.65         #Threshold that is used during validation

    GROUNDTRUTHIMAGES = "./Dataset/"   #location of ground truth images
    GROUNDTRUTHLABELS = "./Labels/"        #location of ground truth labels

    PREDICTIONFINGERPRINT = "Predictions/Fingerprint/"                  #location where fingerprint images will be saved
    PREDICTIONPORE = "Predictions/Pore/"                                # location where pore maps will be saved
    PREDICTIONCOORDINATES = "Predictions/Coordinates/"                  #location where .txt files with pore coordinates will be saved

    TESTIMAGEHEIGHT = 240       # Height of Test Images
    TESTIMAGEWIDTH = 320        # Width of Test Images

    TRAINIMAGEHEIGHT = 240      # Height of Train Images
    TRAINIMAGEWIDTH = 320       # Width of Train Images


    TEST_START_PROBABILITY = 0.3    # Minimum threshold probability that will be checked 
    TEST_END_PROBABILITY = 1.0        # Maximum threshold probability that will be checked
    TEST_STEP = 0.05                # Step while testing threshold probabilities

    TEST_START_NMS = 0.15              # Minimum NMS threshold probability that will be checked  
    TEST_END_NMS = 0.7              # Maximum NMS threshold probability that will be checked
    STEP_NMS = 0.05                 # Step while testing NMS threshold probabilities

    PORELABELRADIUS = 14           # Radius around the center pore that is cosidered to be a pore

    NUMBERLAYERS = 8                # Number of CNN layers
    MAXPOOLING = False              # Is Maxpooling Allowed
    NUMBERFEATURES = 64             # Number of features on each layer

    CRITERIA = "BCELOSS"
    OPTIMIZER = "ADAM"

    TOLERANCE = 2
