from Levenshtein import distance
import click

def check_edit_distance_from_egf(query_sequence):
    wt_sequence = "NSDSECPLSHDGYCLHDGVCMYIEALDKYACNCVVGYIGERCQYRDLKWWELR"

    edit_distance = distance(query_sequence, wt_sequence)
    
    if edit_distance >= 10:
        print(f"The edit distance is at least 10: {edit_distance}")
    else:
        print(f"The edit distance is less than 10: {edit_distance}")

@click.command()
@click.argument("query_sequence")
def main(query_sequence):
    check_edit_distance_from_egf(query_sequence)

if __name__ == "__main__":
    main()
