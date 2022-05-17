# Asistente de voz | jarvis -> Iza
Proyecto para generar acciones mediante comandos de voz, implementando raspberry pi, chimalli y firebase

## Conectar con bocina Bluethoot.
        systemctl is-enabled bluetooth.service
        bluetoothctl
        power on
        agent on
        scan on
        pair <F3:16:E9:1E:CC:5B>
        trust  <F3:16:E9:1E:CC:5B>
        paired-devices
        connect <F3:16:E9:1E:CC:5B>

## Entorno
- Crear entorno.
        
        python -m venv env
        source env/bin/activate

- Después de crear el entorno es necesario instalar.

        sudo apt-get install libffi-dev

        sudo apt-get install libssl-dev

        sudo apt-get install libzbar-dev libzbar0

        python -m pip install --upgrade google-assistant-library google-assistant-sdk[samples]

        python -m pip install --upgrade google-auth-oauthlib[tool]

        google-oauthlib-tool --client-secrets cred.json --scope https://www.googleapis.com/auth/assistant-sdk-prototype --scope https://www.googleapis.com/auth/gcm --save --headless

        sudo apt-get install libportaudio2

        chromium-browser --disable-web-security --user-data-dir '/home/pi'

## Mover archivos de local a raspberry
        scp -r  app  pi@192.168.1.79:Documentos/jarvis

### Pyenv ref
        https://www.liquidweb.com/kb/how-to-install-pyenv-on-ubuntu-18-04/