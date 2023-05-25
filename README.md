# whisper-docker
whisper with docker

## Setup
Install Docker.

```sh
$ git clone https://github.com/karaage0703/whisper-docker
$ cd whisper-docker
$ docker build -t whisper .
```

## Usage
### Voice recognition with microphone
Execute following command in `whisper-docker` directory.

```sh
$ docker run -it -d -v $(pwd):/workspace/ --net host --name whisper whisper
$ docker exec -it whisper bash
root@hostname:/workspace# python whisper-server.py
```

Open new terminal and execute following command:

```sh
$ python mic.py
```

### Transcribe
Prepare audio file (ex: `input.mp3`) and execute following command in `whisper-docker` directory.

```sh
$ docker run -it -d -v $(pwd):/workspace/ --net host --name whisper whisper
$ docker exec -it whisper bash
root@hostname:/workspace# python transcribe.py --model='base' --input_file='input.mp3' --output_file='output.txt' --language='ja'
```

## Reference
- https://zenn.dev/kento1109/articles/d7d8f512802935
