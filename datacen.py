import fiftyone as fo
# import fiftyone.zoo as foz
import fiftyone.utils.huggingface as fouh
 
fo.launch_app()
 
# Load the dataset from Hugging Face if it's your first time using it
 
dataset = fouh.load_from_hub(
    "Voxel51/Coursera_lecture_dataset_train",
    dataset_name="lecture_dataset_train",
    persistent=True
    )
 
test_dataset = fouh.load_from_hub(
    "Voxel51/Coursera_lecture_dataset_test",
    dataset_name="lecture_dataset_test",
    persistent=True
    )
 
dataset.compute_metadata()
 
test_dataset.compute_metadata()
 
cloned_dataset = dataset.clone(name="lecture_dataset_train_clone", persistent=True) #clone the dataset to avoid modifying the original dataset
 
test_dataset = test_dataset.clone(name="lecture_dataset_test_clone", persistent=True)
 
session = fo.launch_app(cloned_dataset)
 
session.wait()





select_tomato_stage = fo.SelectBy("ground_truth.detections.label", "hat")
tomato_view = dataset.add_stage(select_tomato_stage)
tomato_view
tomato_view.count_values("ground_truth.detections.label")
fo.launch_app(tomato_view)
.
