








void MainWindow::save()
{
    QFile file("somefile.bin");
    if (file.open(QIODevice::WriteOnly)) {
        QDataStream stream(&file);
        qint32 n(model->rowCount()), m(model->columnCount());
        stream << n << m;

        for (int i=0; i<n; ++i)
            for (int j=0; j<m; j++)
                model->item(i,j)->write(stream);
        file.close();
    }
}

void MainWindow::load()
{
    QFile file("somefile.bin");
    if (file.open(QIODevice::ReadOnly)) {
        QDataStream stream(&file);
        qint32 n, m;
        stream >> n >> m;

        model->setRowCount(n);
        model->setColumnCount(m);
        for (int i=0; i<n; ++i)
            for (int j=0; j<m; j++)
                model->item(i,j)->read(stream);
        file.close();
    }
}