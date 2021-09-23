import torch

# check PyTorch version & CUDA and CUDNN availability
def main():
    print("PyTorch Version: ", torch.__version__)
    print("CUDA Available: ", torch.cuda.is_available())
    print("CUDNN Available: ", torch.backends.cudnn.enabled)
    
    # generate random tensor using PyTorch
    x = torch.rand(5, 3)
    print("Random Tensor Generated: \n", x)

# run main function
if __name__ == "__main__":
    main()