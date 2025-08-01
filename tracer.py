import argparse
from packages.main import traceroute

if _name_ == "_main_":
  parse = argparse.ArgumentParser()
  # create arguments
  parser.add_argument("destination_server")
  parser.add_argument("-t", "--timeout", required=False, nargs="?",default=5, typw=int, metavar="Tieout in seconds")
  parser.add_argument("-m", "--maxhops", required=False, nargs="?"defaut=30, type=int, metavar="Max hops")

  args = parser.parse_args()
  # destruct the arguments passed
  destination_server, timeout, max_hops = args.destination_server, args.timeout, args.maxhops
  # begin trace
  traceroute(destination_server, max_hops, timeout)
