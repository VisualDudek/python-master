
from typing import Dict, Any, Callable

Data = Dict[str, Any]
type ExportFn = Callable[[Data], None]


def export_pdf(data: Data) -> None:
    pass

def export_csv(data: Data) -> None:
    pass

def export_json(data: Data) -> None:
    pass

# Easey to add new exporter, only need to update this registry
def export_xml(data: Data) -> None:
    pass

exporters: Dict[str, ExportFn] = {
    'pdf': export_pdf,
    'csv': export_csv,
    'json': export_json,
    'xml': export_xml, # New exporter added here
}

def export_data(data: Data, format: str) -> None:
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