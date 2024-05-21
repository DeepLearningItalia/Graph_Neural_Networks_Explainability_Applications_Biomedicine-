# Graph Neural Networks and Explainability: Applications in Biomedicine
Reposity ufficiale del corso DLI di Graph Neural Networks and Explainability: Applications in Biomedicine.

## Per iniziare
La repository contiente un file ```environment.yml``` con tutti i pacchetti necessari per far funzionare i nootebook delle lezioni. Avendo [Anaconda](https://www.anaconda.com/) installato sul proprio computer, è possibile create un environment dal file. Aprite il file e modificate il parametro ```prefix``` con il percorso nel quale sono salvati i vostri enrivornment e lanciate da terminale:

```bash
conda env create -f environment.yml
```
Quando tutti i pacchetti saranno stati installati, attivate l'environment:

```bash
conda activate GNN_XAI_Biomedicine_env
```
Il nome di default dell'environment (GNN_XAI_Biomedicine_env) può essere modificato a piacimento.

## Contenuto
La repository contiene 6 notebook Python che seguondo le lezioni presentate nel corso. In particolare:

1. ```1-gene_disease_associations_via_GNNs.ipynb```: definizione, training e utilizzo di una graph neural network per la task di disease gene association discovery utilizzando una protein-protein interaction (PPI) network.
2. ```compound_activity_prediction_via_GNNs.ipynb```: definizione, training e utlizzo di una graph neural network per la task di compound activity predicion utilizzando dati molecolari.
3. ```3-protein_ligand_affinity_prediction_via_GNN.ipynb```: definizione, training e utilizzo di una graph neural network per la task di compound potency predicion utilizzando protein-ligand interaction graphs.
4. ```4-explaining_gene_disease_prioritization.ipynb```: utilizzo di XAI per spiegare le predizioni della graph neural network utlizzata per disease gene association discovery.
5. ```5-explaining_compound_activity_predictions.ipynb```: utilizzo di XAI per spiegare le predizioni della graph neural network utlizzata per compound activity predicion.
6. ```6-explaining_compound_potency_predictions.ipynb```: utilizzo di XAI per spiegare le predizioni della graph neural network utlizzata per compound potency predicion.

## Docente

<div style="display: flex; align-items: flex-start;">
  <img src="https://lh5.googleusercontent.com/wCtbF5xRfkNjrrjzW_5Pyg3_YPM8c85lcJNZZ4HmE5cAd_JhGZQ5_Th2Xv9ddjIahmo8-aZZkYGNQH7eiadrGeTHdoeqNzNTXdIvIoX2MWRORThUUdgK9j9pI3qaWebtXw=w1280" alt="Description" style="width: 200px; margin-right: 10px;">
  <span>Mi chiamo Andrea Mastropietro, sono un ingegnere informatico, data scientist e ricercatore in biomedical artificial intelligence. Sono laureato in Ingegneria Informatica e Automatica (triennale) alla Sapienza e Engineering in Computer Science (magistrale) nella stessa università. La passione per la ricerca e per l’impatto che essa può avere mi ha portato a conseguire un dottorato in Data Science con una tesi dal titolo “Toward Explainable Biomedical Deep Learning – Training and Explaining Neural Networks in Bioinformatics and Medicinal Chemistry”. Durante il mio dottorato, ho svolto un periodo di ricerca all’Università di Bonn in Germania. La mia attività di ricerca si basa sull’applicazione dell’intelligenza artificiale, in particolare del deep learning, in ambito biomedico, bioinformatico e chemoinformatico, con un focus particolare sullo sviluppo ed utilizzo di tecniche di explainable artificial intelligence (XAI), per aprire la “black box” di questi sistemi e renderli più utilizzabili in biomedicina.
</span>
</div>

## Contatti e links

[![Website Badge](https://img.shields.io/badge/mastro.me-orange?style=flat&logoSize=auto&label=website&labelColor=orange&color=darkred&link=http://mastro.me)](http://mastro.me)
[![email Badge](https://img.shields.io/badge/email-white?style=flat&logo=gmail&logoSize=auto)](mailto:mastropietro@diag.uniroma1.it)
[![github](https://img.shields.io/badge/AndMastro-100000?style=flat&logo=github&logoColor=white)](https://github.com/AndMastro)
[![LinkedIn Badge](https://img.shields.io/badge/Andrea%20Mastropietro-blue?style=flat&logo=linkedin&logoSize=auto&labelColor=blue&color=blue&link=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fandrea-mastropietro%2F)](https://www.linkedin.com/in/andrea-mastropietro/)
[![X (formerly Twitter) URL](https://img.shields.io/twitter/url?url=https%3A%2F%2Fx.com%2FAndMastro&logo=twitter&logoSize=auto&label=AndMastro&link=https%3A%2F%2Fx.com%2FAndMastro)](https://x.com/AndMastro)
[![RG Badge](https://img.shields.io/badge/Andrea%20Mastropietro-grey?style=flat&logo=researchgate&logoSize=auto&link=https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FAndrea-Mastropietro)](https://www.researchgate.net/profile/Andrea-Mastropietro)
