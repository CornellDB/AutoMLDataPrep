import pandas as pd
import numpy as np
import random
import string

def add_gaussian_noise(text, mean=0, std_dev=0.1):
    """
    Add Gaussian noise to text.
    
    Parameters:
        text (str): The input text to which noise will be added.
        mean (float): Mean of the Gaussian distribution.
        std_dev (float): Standard deviation of the Gaussian distribution.
    
    Returns:
        str: The text with added Gaussian noise.
    """
    noisy_text = list(text)
    
    # Generate Gaussian noise with the same length as the text
    noise = np.random.normal(mean, std_dev, len(noisy_text))
    
    for i in range(len(noisy_text)):
        noisy_text[i] = chr(ord(noisy_text[i]) + int(noise[i]))
    
    return ''.join(noisy_text)

def add_random_noise(text, noise_level):
    """
    Add random noise to text.
    
    Parameters:
        text (str): The input text to which noise will be added.
        noise_level (int): Value between 0 and 1 signifying level of noise.
    
    Returns:
        str: The text with added random noise.
    """
    noise_len = int(len(text) * noise_level)

    if noise_len == 0:
        return text
   
    noise_indices = random.sample(range(len(text)), noise_len)
   
    noisy_text = list(text)
 
    for idx in noise_indices:
        noisy_text[idx] = random.choice(string.ascii_letters)
    return ''.join(noisy_text)