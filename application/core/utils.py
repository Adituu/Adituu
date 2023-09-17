from typing import Union

def size_convert(num: int, suffix: str = 'B') -> str:
    # https://web.archive.org/web/20111010015624/http://blogmag.net/blog/read/38/Print_human_readable_file_size

    for unit in ['', ' Ki', ' Mi', ' Gi', ' Ti', ' Pi', ' Ei', ' Zi']:
        if abs(num) < 1024.0:
            return f'{num:3.1f}{unit}{suffix}'
        num /= 1024.0

    return f'{num:.1f}Yi{suffix}'


def allowed_file_extension(filename: str, allowed_extensions: Union[list, tuple]) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
