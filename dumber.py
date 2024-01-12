# Import libraries for knowledge graphs
import pprint
from rdflib import Graph
from rdflib import ConjunctiveGraph
import os
from tqdm import tqdm
import sys
import argparse
def merge_ttl_files(folder_path, output_file, limit=None):
    # Crea un grafo RDF congiuntivo per il merge di tutti i file TTL
    merged_graph = ConjunctiveGraph()

    # Itera attraverso i file nella cartella
    file_count = 0
    for filename in tqdm(os.listdir(folder_path)):
        if limit is not None and file_count >= limit:
            break

        if filename.endswith(".ttl"):
            file_path = os.path.join(folder_path, filename)
            
            # Carica il contenuto del file nel grafo RDF
            with open(file_path, "r") as file:
                ttl_data = file.read()
                graph = Graph()
                graph.parse(data=ttl_data, format="turtle")

                # Aggiungi il grafo corrente al grafo congiuntivo
                merged_graph += graph

            file_count += 1

    merged_graph.serialize(destination=output_file, format="turtle")

if __name__ == "__main__":
    # Parse the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_path", help="Path to the folder containing TTL files")
    parser.add_argument("output_file", help="Output file name")
    parser.add_argument("--limit", type=int, help="Limit the number of files to merge")
    args = parser.parse_args()

    merge_ttl_files(args.folder_path, args.output_file, args.limit)

    print(f"I file TTL nella cartella sono stati uniti con successo in {args.output_file}.")



