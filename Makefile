PROB ?= 2091
LANG ?= py

rust:
	rustc "$(PROB)/main.rs" -o "/tmp/$(PROB)" && "/tmp/$(PROB)"

java:
	cd "$(PROB)" && javac Main.java && java Main

new:
	@mkdir -p "$(PROB)"
	@case "$(LANG)" in \
		cpp|c++) \
			FILE="$(PROB)/main.cpp"; \
			printf '#include <iostream>\n\nint main() {\n    return 0;\n}\n' > "$$FILE"; \
			;; \
		java) \
			FILE="$(PROB)/Main.java"; \
			printf 'public class Main {\n    public static void main(String[] args) {\n\n    }\n}\n' > "$$FILE"; \
			;; \
		py|python|python3) \
			FILE="$(PROB)/main.py"; \
			printf 'def main():\n    pass\n\n\nif __name__ == "__main__":\n    main()\n' > "$$FILE"; \
			;; \
		js|javascript) \
			FILE="$(PROB)/main.js"; \
			printf '"use strict";\n\nfunction main() {\n}\n\nmain();\n' > "$$FILE"; \
			;; \
		cs|csharp|c\#) \
			FILE="$(PROB)/Program.cs"; \
			printf 'using System;\n\nclass Program\n{\n    static void Main()\n    {\n    }\n}\n' > "$$FILE"; \
			;; \
		c) \
			FILE="$(PROB)/main.c"; \
			printf '#include <stdio.h>\n\nint main(void) {\n    return 0;\n}\n' > "$$FILE"; \
			;; \
		go) \
			FILE="$(PROB)/main.go"; \
			printf 'package main\n\nfunc main() {\n}\n' > "$$FILE"; \
			;; \
		rs|rust) \
			FILE="$(PROB)/main.rs"; \
			printf 'fn main() {\n    println!("Hello, world!");\n}\n\nstruct Solution;\n\n// Solution:\nimpl Solution {\n}\n' > "$$FILE"; \
			;; \
		*) \
			echo "Unsupported language: $(LANG)"; \
			echo "Supported: cpp java py js cs c go rust"; \
			exit 1; \
			;; \
	esac; \
	echo "Created $$FILE"