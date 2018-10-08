import arviz as az
non_centered = az.load_arviz_data('non_centered_eight')
az.plot_posterior(non_centered)
