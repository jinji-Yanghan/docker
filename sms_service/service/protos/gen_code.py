from grpc.tools import protoc

if __name__ == '__main__':
    protoc.main(
        (
            '',
            '-I.',
            '--python_out=../',
            '--grpc_python_out=../',
            './sms.proto',
        )
    )
