# Manage JS and CSS
## Setup
`npm` is required on the system.

To install the dependencies, run:
```bash
cd frontend
npm install
```

## Collect and pack JS+CSS
Run
```bash
cd frontend
npm run build
```

This will create `bundle.js` and some other files in `ScanCraft/static/build`.


# Rename the Sekelton
```bash
old_string='ScanCraft'
new_string='LabelCraft'
startdir='.'

# Replace strings in files
grep -rl "$old_string" "${startdir}" | xargs sed -i "s/$old_string/$new_string/g"

# Rename files
find "${startdir}" -name "*$old_string*" -type f |
while read -r fname; do
  mv "$fname" "$(echo $fname | sed "s/$old_string/$new_string/g")"
done

# Rename directories
find "${startdir}" -name "*$old_string*" -type d |
while read -r dname; do
  mv "$dname" "$(echo $dname | sed "s/$old_string/$new_string/g")"
done

```