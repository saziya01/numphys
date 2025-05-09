import random 
from estimatePi import estimate_pi

def test_main():
    num_samples = int(input("Enter total number of points:"))
    estimated_pi = estimate_pi(num_samples)

    print(estimated_pi)
    
if __name__ == "__main__":
 test_main()