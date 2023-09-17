import re
import requests
import unittest

def get_pincode_from_address(address):
    # Extract the pincode from the address using regex
    ## I have assumed here that there are no other digits included in the address with length 6 apart from pincode.
    
    extracted_pincode = re.findall(r"\d{6}", address)
    print(extracted_pincode)
    if not extracted_pincode:
        raise ValueError("Pincode not found in the input address.")
    
    url = f"https://api.postalpincode.in/pincode/{extracted_pincode[0]}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        if data and data[0]["Status"] == "Success":
            return data[0]["PostOffice"][0]["Name"]
        else:
            raise ValueError("Invalid pincode.")
    
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to connect: {str(e)}")
    except (ValueError, KeyError) as e:
        raise ValueError(f"Error: {str(e)}")

if __name__ == "__main__":
    input_address = "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050"
    
    try:
        pincode_info = get_pincode_from_address(input_address)
        print(f"Post Office Name: {pincode_info}")
    except (ValueError, ConnectionError) as e:
        print(f"Error: {str(e)}")


## for test cases using the unittest package.
class TestGetPincodeFromAddress(unittest.TestCase):
    def test_valid_address(self):
        address = "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Ashoknagar (Bangalore), Bengaluru, Karnataka 560050"
        result = get_pincode_from_address(address)
        self.assertEqual(result, "Ashoknagar (Bangalore)")

    def test_invalid_pincode(self):
        address = "Invalid address without pincode"
        with self.assertRaises(ValueError):
            get_pincode_from_address(address)


    def test_wrong_pincode_value_error(self):
        address = "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 999999"
        with self.assertRaises(ValueError):
            get_pincode_from_address(address)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)