phone_numbers = {
  'Aakash' : '9489484949',
  'Hemanth' : '9595949494',
  'Siddhant' : '9231325312'
}
phone_numbers

phone_numbers['Aakash']

# Add a new value
phone_numbers['Vishal'] = '8787878787'
# Update existing value
phone_numbers['Aakash'] = '7878787878'
# View the updated dictionary
phone_numbers

for name in phone_numbers:
    print('Name:', name, ', Phone Number:', phone_numbers[name])