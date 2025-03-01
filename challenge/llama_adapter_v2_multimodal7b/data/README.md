---
license: cc-by-nc-sa-4.0
viewer: false
---
# **DriveLM:** Driving with **G**raph **V**isual **Q**uestion **A**nswering.

We facilitate `Perception, Prediction, Planning, Behavior, Motion` tasks with human-written reasoning logic as a connection. We propose the task of GVQA to connect the QA pairs in a graph-style structure. To support this novel task, we provide the DriveLM-Data. 

DriveLM-Data comprises two distinct components: DriveLM-nuScenes and DriveLM-CARLA. In the case of DriveLM-nuScenes, we construct our dataset based on the prevailing nuScenes dataset. As for DriveLM-CARLA, we collect data from the CARLA simulator.

## Prepare DriveLM-nuScenes Dataset

Our DriveLM-nuScenes contains a collection of questions and answers. The dataset is named `v1_0_train_nus.json`. We offer a subset of image data that includes all the images used in our DriveLM. You can also download the full nuScenes dataset [HERE](https://www.nuscenes.org/download). 

## Usage

1. Download nuScenes subset image data (or full nuScenes dataset) and `v1_0_train_nus.json`.

2. Organize the data structure as follows:

```
DriveLM
├── data/
│   ├── QA_dataset_nus/
│   │   ├── v1_0_train_nus.json
│   ├── nuscenes/
│   │   ├── samples/
```

## Prepare DriveLM-CARLA Dataset
We provide a collection of questions and answers for DriveLM-CARLA. The dataset `drivelm_carla_vqas.zip` contains question-answer pairs for pre-determined keyframes listed in `drivelm_carla_keyframes.txt` for each scenario. You can download the full dataset using the provided [script](https://github.com/OpenDriveLab/DriveLM/blob/DriveLM-CARLA/vqa_dataset/download_pdm_lite_carla_lb2.sh). All scripts for extracting keyframes and generating the question-answer dataset are available on [GitHub](https://github.com/OpenDriveLab/DriveLM/blob/DriveLM-CARLA/vqa_dataset). Additionally, we also provide instructions how to built your own dataset.

## License and Citation

This language dataset is licensed under [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). If you use this dataset, please cite our work: 


```BibTeX
@article{drivelm_paper2023,
  title={DriveLM: Driving with Graph Visual Question Answering},
  author={Sima, Chonghao and Renz, Katrin and Chitta, Kashyap and Chen, Li and Zhang, Hanxue and Xie, Chengen and Luo, Ping and Geiger, Andreas and Li, Hongyang},
  journal={arXiv preprint arXiv:2312.14150},
  year={2023}
}
```

```BibTeX
@misc{drivelm_repo2023,
  title={DriveLM: Driving with Graph Visual Question Answering},
  author={DriveLM contributors},
  howpublished={\url{https://github.com/OpenDriveLab/DriveLM}},
  year={2023}
}
```

For more information and updates, please visit our [GitHub repository](https://github.com/OpenDriveLab/DriveLM).

