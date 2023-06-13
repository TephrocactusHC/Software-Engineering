import pylint.lint

pylint_opt = ['-ry', './max_product.py']
pylint.lint.Run(pylint_opt)