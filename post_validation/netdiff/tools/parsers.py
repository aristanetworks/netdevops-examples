import argparse

def src_dst_parser():
    parser = argparse.ArgumentParser(description='=== A NetDiff Module Help ===', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--src_filename', '-src', help='Source filename.', required=True)
    parser.add_argument('--dst_filename', '-dst', help='Destination filename.', required=True)
    parser.add_argument('--src_format', '-sfm', choices=['yaml', 'json', 'csv'], default='yaml', help='Source file format')
    parser.add_argument('--dst_format', '-dfm', choices=['yaml', 'json', 'csv'], default='yaml', help='Destination file format')
    parser.add_argument('--case', '-c', help='Name of the data processing function.', required=True)
    
    return parser.parse_args()