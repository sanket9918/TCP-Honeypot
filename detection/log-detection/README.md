## Usage
### Encode your http logs and save the result into a csv file
<code> $ python3 data-augment.py -l ./data/apr-2021.log -d ./labeled-data/apr-2021.csv</code>

### Train a model and test the prediction
<code> $ python3 model.py -t ./labeled-data/all.csv -v ./labeled-data/apr-2021.csv </code>

Source of the data  - http://www.secrepo.com/self.logs/