## Usage
### Encode your http logs and save the result into a csv file
<code> $ python3 data-augment.py -l ./data/access-2018-12-15.log -d ./labeled-data/access-2018-12-15.csv</code>

### Train a model and test the prediction
<code> $ python3 model.py -t ./labeled-data/all.csv -v ./labeled-data/access-2018-12-15.csv </code>

Source of the data  - http://www.secrepo.com/self.logs/