#! /usr/bin/env python3

import os
import sys

def main():
    machine = sys.argv[1]
    experiment = os.getcwd().split("/")[-2].split(".")[0]
    with os.scandir(".") as it:
        for entry in it:
            if entry.is_file():
                with open(entry, 'r') as file:
                    print_string =""
                    data = file.read()
                    if(machine == "lassen"):
                        nodes, data, _ = data.split("Modules")
                        nodes = nodes.split(":")[-1].strip()
                    else:
                        nodes, data = data.split("Modules")
                        nodes = nodes.split(":")[1].strip()
                    MPI, data = data.split("\n",1)
                    MPI = MPI.lstrip(': ')
                    for matrix in data.split("Starting ")[1:]:
                        matrix_name, matrix = matrix.split("\n",1)
                        matrix_name.strip()
                        form_time = 0.0
                        p2p_time  = 0.0
                        mpi_time  = 0.0
                        mpix_time = 0.0
                        for line in matrix.split("\n"):
                            if "form: " in line:
                                form_time += float(line.rstrip().split(": ")[1])
                            elif "Standard comm:" in line:
                                p2p_time += float(line.rstrip().split(": ")[1])
                            elif "Standard graph" in line or "Standard neighbor: " in line:
                                mpi_time += float(line.rstrip().split(": ")[1])
                            elif "advance" in line:
                                mpix_time += float(line.rstrip().split(": ")[1])

                        print(machine,nodes,matrix_name,MPI,experiment,p2p_time,mpi_time,mpix_time,sep=",")
                    print(print_string, end="")


if __name__ == "__main__":
	main()
