    '''
    TASK-02
    Develop a simple image encryption tool using pixel manipulation.
    Support operations like swapping pixel valus or applying 
    a basic  mathematical operation to each pixel.'''
    #made by Ashwak_N

    from PIL import Image
    import numpy as np

    def encrypt_image(image_path, key):
    
        img = Image.open(image_path)
        

        img_array = np.array(img)

    
        key = np.resize(key, img_array.shape)

    
        encrypted_array = np.bitwise_xor(img_array, key)
        
        
        encrypted_img = Image.fromarray(encrypted_array)
        
        
        encrypted_img.save("encrypted_image.png")
        print("Image encrypted successfully.")


    def decrypt_image(encrypted_image_path, key):
    
        encrypted_img = Image.open(encrypted_image_path)
        
    
        encrypted_array = np.array(encrypted_img)

        key = np.resize(key, encrypted_array.shape)

        decrypted_array = np.bitwise_xor(encrypted_array, key)
        
    
        decrypted_img = Image.fromarray(decrypted_array)
        

        decrypted_img.save("decrypted_image.png")
        print("Image decrypted successfully.")

    # D:\Image\image.png

    def main():
        print("Image Encryption and Decryption using Pixel Manipulation")

        
        image_path = input("Enter thepip path to the image file: ")
        
        key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)
        
    
        encrypt_image(image_path, key)
        
        
        decrypt_image("encrypted_image.png", key)

    if __name__ == "__main__":
        main()

