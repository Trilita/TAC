cat /Users/javierhonduco/Downloads/primes1.txt | tail -n +3 | tr '[:space:]' '\n' | sed '/^$/d' > primes/all_primes_mit.txt
