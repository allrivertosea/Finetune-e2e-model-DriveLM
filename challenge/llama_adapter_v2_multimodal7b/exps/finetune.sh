#!/usr/bin/bash
export CUDA_VISIBLE_DEVICES="0" 
export CUDA_DEVICE_MAX_CONNECTIONS=1

python -u \
 main_finetune.py \
 --data_config "/APP/DriveLM/challenge/llama_adapter_v2_multimodal7b/finetune_data_config.yaml" \
 --batch_size 1 \
 --epochs 4 \
 --warmup_epochs 1 \
 --blr 10e-4 \
 --weight_decay 0.02 \
 --llama_path "/APP/DriveLM/challenge/model_weights/llama_model_weights" \
 --output_dir "/APP/DriveLM/outputs" \
 --pretrained_path "/APP/DriveLM/challenge/model_weights/LLaMA-Adapter_V2/7fa55208379faf2dd862565284101b0e4a2a72114d6490a95e432cf9d9b6c813_BIAS-7B.pth" \
 &>> "/APP/DriveLM/outputs/output.log" &