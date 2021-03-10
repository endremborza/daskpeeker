Quickstart
==========

.. code:: ipython3

    from daskpeeker import Peeker, Metric

.. code:: ipython3

    import dask.dataframe as dd
    import pandas as pd

.. code:: ipython3

    class MyPeeker(Peeker):
        
        def get_shared_figures(self):
            pass
            return []
        
        def get_report_elems(self, filtered_ddf):
            
            return [Metric(filtered_ddf.loc[:, "n1"].mean().compute(), "Average N1")]

.. code:: ipython3

    df = pd.DataFrame({"n1": [1, 2, 3, 4], "c1": list("ABCD")})
    
    ddf = dd.from_pandas(df, npartitions=4).persist()

``peeker = MyPeeker(ddf, ["c1"], ["n1"])``

``peeker.run(port_no=5678, debug=False)``
