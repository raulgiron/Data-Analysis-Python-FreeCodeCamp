# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

print(mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Run unit tests automatically
main(module='test_module', exit=False)

# https://replit.com/@raulgiron1/boilerplate-mean-variance-standard-deviation-calculator-1?v=1
