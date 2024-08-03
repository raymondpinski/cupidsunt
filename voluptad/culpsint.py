l_ms = metadata.get('duration', None)
if l_ms is not None:
    print(f"Duration in milliseconds: {l_ms}")
else:
    print("Duration key not found in metadata.")
