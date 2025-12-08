.PHONY: demo test

demo:
	cd .. && source .venv/bin/activate && python -m final_project.demo_runner

test:
	cd .. && source .venv/bin/activate && python -m unittest final_project.sorting_test -v

