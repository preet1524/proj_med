
import pickle
import json
import pandas as pd
import numpy as np



class HousePrice():
    def __init__(self,size,bath,balcony,area_type,location):
        self.size = size
        self.bath = bath
        self.balcony = balcony
        
        self.area_type = "area_type_" + area_type
        self.location = "location_"+ location
       

    def load_model(self):
        with open('models/Bengaluru_House_data.pkl', "rb") as f:
            self.model = pickle.load(f)

        with open('models/project_data.json',"r") as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):

        self.load_model()        # method to get model and json_data

        area_type_index = self.json_data['column'].index(self.area_type)
        location_index = self.json_data['column'].index(self.location)
        array = np.zeros(len(self.json_data['column']))

        array[0]= self.size
        array[1]= self.bath
        array[2]= self.balcony
        array[area_type_index]= 1
        array[location_index] = 1

        print("Test Array -->\n",array)
        predicted_charges = self.model.predict([array])[0]
        print("predicted_house",predicted_charges)
        return np.around(predicted_charges, 2)


if __name__ == "__main__":
    size = 2.0
    bath = 2.0
    balcony = 1.0
    

    # one hot encoded values
    area_type="Built-up  Area"
    location="Kothanur"
    
    predict_price = HousePrice(size,bath,balcony,area_type,location)
    charges = predict_price.get_predicted_price()
    print()
    print(f"The House Price in Bengaluru is {charges} Rs-\ Only(Lakh)")