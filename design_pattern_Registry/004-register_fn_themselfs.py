from typing import Dict, Any, Callable
from functools import wraps

Data = Dict[str, Any]
type ExportFn = Callable[[Data], None]

exporters: Dict[str, ExportFn] = {}

# Decorator to register exporter functions
def register_exporter(format: str) -> Callable[[ExportFn], ExportFn]:
    def decorator(fn: ExportFn) -> ExportFn:
        exporters[format] = fn

        @wraps(fn)
        def wrapper(data: Data) -> None:
            return fn(data)

        return wrapper

    return decorator

@register_exporter('pdf')
def export_pdf(data: Data) -> None:
    print("Exporting data as PDF")

@register_exporter('csv')
def export_csv(data: Data) -> None:
    print("Exporting data as CSV")

@register_exporter('json')
def export_json(data: Data) -> None:
    print("Exporting data as JSON")

@register_exporter('xml')
def export_xml(data: Data) -> None:
    print("Exporting data as XML")


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