from ultralytics import YOLO

def first():
  # Load a model
  model = YOLO('yolov8n.yaml')  # build a new model from YAML
  # model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
  # model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights
  
  # Specify the output directory and project name
  output_directory = "/content/drive/MyDrive/data_for_models/pipe_counting_number_wise_num-4"  # Replace with your desired output directory
  project_name = "yolov8n_mul_cls_sing_model"  # Replace with your desired project name
  
  # Train the model
  results = model.train(data="/content/drive/MyDrive/data_for_models/pipe_counting_number_wise_num-4/data.yaml", epochs=200, imgsz=640,project=output_directory,
                        name=project_name)

def second():
    # Load a model
    # model = YOLO('yolov8m.yaml')  # build a new model from YAML
    model = YOLO('yolov8m.pt')  # load a pretrained model (recommended for training)
    # model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

    # Specify the output directory and project name
    output_directory = r"E:\yolo_training\filter open_pleat.v1i.yolov8"  # Replace with your desired output directory
    project_name = "medium_modell"  # Replace with your desired project name

    # Train the model
    results = model.train(data="data.yaml", epochs=200, imgsz=640,project=output_directory,
                        name=project_name,batch=8,workers=4)
