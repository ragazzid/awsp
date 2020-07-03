# awsp
A simple parser to export sts assume role output to export bash :)

## Usage
```
aws sts assume-role --role-arn arn:aws:iam::XXXXXXXXXXXXXXXXXX:role/tmp --role-session-name xtpo | awsp        
export AWS_ACCESS_KEY_ID=AAAAAAAAAAAAAAAAAA
export AWS_SECRET_ACCESS_KEY=AAAAAAAAAAAAAAAAAA/AAAAAAAAAAAAAAAAAA
export AWS_SESSION_TOKEN="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
```

Or, directly to your env variables

```
eval $(aws sts assume-role --role-arn arn:aws:iam::XXXXXXXXXXXXXXXXXX:role/tmp -role-session-name xtpo | awsp)
```

Then

```
aws sts get-caller-identity
{
    "Account": "XXXXXXXXXXXXXXXXXX", 
    "UserId": "YYYYYYYYYYYYYY:xtpo", 
    "Arn": "arn:aws:sts::XXXXXXXXXXXXXXXXXX:assumed-role/tmp/xtpo"
}

```

# Build & Send
```
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository testpypi dist/*
```