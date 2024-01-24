# spotycli

A cli tool to interact with your spotify account

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)

## Installation

> Disclaimer: this tool is in a very early stage in the development so client id and client secret are not provided. To test the this tool register at [spotify for developer](https://developer.spotify.com/), create an app and paste the client id and client secret in [spoty_client.py](spoty_client.py)

Clone this repository

```zsh
git clone https://github.com/micheledinelli/spotycli.git
```

Change directory where you cloned the repository and install the dependencies

```zsh
pip install -r requirements.txt
```

Run it with

```zsh
python .\main.py --help
```

A facade is provided to run the application

```zsh
chmod +x spotycli
```

Inside the .zshrc or .bashrc add

```zsh
export PATH=$PATH:/your/full/path/to/the/project
```

And then you can run the application with

```zsh
spotycli --help
```

## Preview

Getting help and showing the current user

![Image](https://private-user-images.githubusercontent.com/95191347/299033915-c9ecdf22-314b-4915-bf00-e18411745c8a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDYwMjk1MjgsIm5iZiI6MTcwNjAyOTIyOCwicGF0aCI6Ii85NTE5MTM0Ny8yOTkwMzM5MTUtYzllY2RmMjItMzE0Yi00OTE1LWJmMDAtZTE4NDExNzQ1YzhhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMjMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTIzVDE3MDAyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI1MTk1YTgyMWZhZTcwNjc0NWI0ODE3MTMzMjJmYjhjMzQ3MzY1NTkxZTdjYWRjZjU2MDVhMzk4OWJjOGMyZmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.DlUVWXN5Ec7VAix-uCWYbCnFTKPImNrtftPrVSEbMXY)

Searching for songs

![Image](https://private-user-images.githubusercontent.com/95191347/299033311-dbd7c1fb-5cdf-4511-8cfc-df29e7af5631.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDYwMjk0MTEsIm5iZiI6MTcwNjAyOTExMSwicGF0aCI6Ii85NTE5MTM0Ny8yOTkwMzMzMTEtZGJkN2MxZmItNWNkZi00NTExLThjZmMtZGYyOWU3YWY1NjMxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMjMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTIzVDE2NTgzMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWFkMzA4Y2RmMjBmMTUzNmE5N2UxYWZmNWJjYmIwMjUzMDg5NWVhYzQ5YThjZDNmZDJiMWNjZTFjNmE0YWYwMDAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.f4IR9r0p-nhZT2Y4QK6OzmZ2jWQPSILbApHBwcfnYrM)
