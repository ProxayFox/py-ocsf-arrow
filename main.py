from py_ocsf_arrow import TypeMapper


if __name__ == "__main__":
    # Example usage of TypeMapper
    type_mapper = TypeMapper.init(version="default")

    print("OCSF to Arrow Type Mapping:")
    for ocsf_type, arrow_type in type_mapper.OCSF_TO_ARROW.items():
        print(f"{ocsf_type} -> {arrow_type}")
