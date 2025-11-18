
from typing import Dict, Any, Callable

Data = Dict[str, Any]
type ExportFn = Callable[[Data], None]


def export_pdf(data: Data) -> None:
    pass

def export_csv(data: Data) -> None:
    pass

def export_json(data: Data) -> None:
    pass

# Registry mapping format strings to exporter functions
exporters: Dict[str, ExportFn] = {
    'pdf': export_pdf,
    'csv': export_csv,
    'json': export_json,
}

def export_data(data: Data, format: str) -> None:
    # Refactored to use the registry
    exporter_fn = exporters.get(format)

    if exporter_fn is None:
        raise ValueError(f'Unsupported format: {format}')

    exporter_fn(data)


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