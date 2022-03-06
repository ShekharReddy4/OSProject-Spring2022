"""Utility functions for parsing files in Linux /proc (procfs) filesystem
"""

def extract_fields(filename, field_struct, delimiter=None):
    """Extract fields from a one-liner file of values and return a generator

    The function extracts fields specified via 'field_struct' parameter from
    a text file passed as 'filename' that contains one line of values
    separated by 'delimiter'. If delimiter is None, the values are assumed to
    be separated as one or more white-space characters.

    Parameters:
    ----------
       - filename: a string representing path to the file

       - field_struct: a tuple (or any iterable) of tuple representing each
                       field to be extracted. each field must be of the form
                       ("Description string", index, data_type)

       - delimiter: a string representing the delimiter for each field.
                    If None, assume variable white-space delimiter.

    Returns:
    -------
    A generator of tuples of the form ("Description string", value)
    """
    with open(filename) as infile:
        fields = infile.readline().split(delimiter)

    return ((description, dtype(fields[index-1]))
            for description, index, dtype in field_struct)


def get_field(filename, field_num, delimiter=None):
    """Return a field from a one-liner file of values as a string

    This function extracts a particular field specified via `field_num` parameter from
    a text file passed as `filename` that contains one line of values separated by
    `delimiter`. If delimiter is None, the values are assumed to
    be separated as one or more white-space characters.

    Parameters:
    ----------
       - filename: a string representing path to the file (str).

       - field_num: an integer representing the field number to be
                       extracted (int).

       - delimiter: a string representing the delimiter for each field.
                    If None, assume variable white-space delimiter (str).

    Returns:
    -------
    a string representing the value (str).
    """
    with open(filename) as infile:
        return infile.readline().split(delimiter)[field_num-1]


def parse_command_line(help):
    """Parse command-line arguments looking up for process pid as argument."""

    from argparse import ArgumentParser
    parser = ArgumentParser(description=help)
    
    parser.add_argument("pid", help="PID of the target process")
    
    return parser.parse_args()

def print_proc_stats(pid, filename, field_struct, unit):
    """Print process-related statistics for a given `pid` based on `field_struct` from a `stat_file`"""

    proc_file = f"/proc/{pid}/{filename}"
    field_values = list(extract_fields(proc_file, field_struct))
    dwidth = max(len(f[0]) for f in field_values)
    iwidth = max(len(str(f[1])) for f in field_values)

    for description, value in field_values:
        print(f"{description:<{dwidth}}: {value:>{iwidth}} {unit}")