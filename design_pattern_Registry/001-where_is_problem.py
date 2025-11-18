
from typing import Dict, Any, Callable

Data = Dict[str, Any]


def export_pdf(data: Data) -> None:
    pass

def export_csv(data: Data) -> None:
    pass

def export_json(data: Data) -> None:
    pass


def export_data(data: Data, format: str) -> None:
    # This is the problem: a big conditional block
    if format == 'pdf':
        export_pdf(data)
    elif format == 'csv':
        export_csv(data)
    elif format == 'json':
        export_json(data)
    else:
        raise ValueError(f'Unsupported format: {format}')


def main():
    sample_data: Data = {
        'name': 'Alice',
        'age': 30,
    }

    export_data(sample_data, 'pdf')
    export_data(sample_data, 'csv')
    export_data(sample_data, 'json')


if __name__ == '__main__':
    main()