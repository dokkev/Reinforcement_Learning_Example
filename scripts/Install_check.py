import torch

# check PyTorch version & CUDA and CUDNN availability
def main():
    print("PyTorch Version: ", torch.__version__)
    print("CUDA Available: ", torch.cuda.is_available())
    print("CUDNN Available: ", torch.backends.cudnn.enabled)
    


if __name__ == "__main__":
    main()