# Name_Validation

<!-- Installation -->
## Installation

run the following command to bulid docker image and start the server
```sh
docker-compose up --build -d
  ```
  
  
  
  
  ![image](https://user-images.githubusercontent.com/101316217/206884574-1e1a7491-9dae-4859-b1ec-859b009de3b4.png)
  
  
  
  ![image](https://user-images.githubusercontent.com/101316217/206884582-d2daf0df-8940-4f23-9e92-b05b8b467fc7.png)
  
  
  
  
  ![image](https://user-images.githubusercontent.com/101316217/206884588-a75730d0-54ec-495f-b59d-f5b41aa2d266.png)
  
  
  
  ![image](https://user-images.githubusercontent.com/101316217/206884598-eab0739b-9119-43b3-a2a6-cc61b890cf14.png)

## Training  

The model trained on 2M example (Fake and Real Names)

num_epochs = 5

## Results 

Training loss: 0.1828 - accuracy: 0.9318 - val_loss: 0.1840 - val_accuracy: 0.9317

## Datasets sources 

http://www.kalmasoft.com/KMAPS/molindx.htm

## Future Work

deal with the validation cases where the father and grandfather must be male 







