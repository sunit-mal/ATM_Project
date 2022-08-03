<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(Form1))
        Me.IDLabel = New System.Windows.Forms.Label()
        Me.IdBox = New System.Windows.Forms.TextBox()
        Me.PasswordLabel = New System.Windows.Forms.Label()
        Me.PasswordBox = New System.Windows.Forms.TextBox()
        Me.RobotCheck = New System.Windows.Forms.CheckBox()
        Me.SubmitButton = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'IDLabel
        '
        Me.IDLabel.AutoSize = True
        Me.IDLabel.BackColor = System.Drawing.SystemColors.ControlLight
        Me.IDLabel.Font = New System.Drawing.Font("Times New Roman", 12.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
        Me.IDLabel.Location = New System.Drawing.Point(156, 132)
        Me.IDLabel.Name = "IDLabel"
        Me.IDLabel.Size = New System.Drawing.Size(100, 26)
        Me.IDLabel.TabIndex = 0
        Me.IDLabel.Text = "Login Id"
        '
        'IdBox
        '
        Me.IdBox.BackColor = System.Drawing.Color.FromArgb(CType(CType(224, Byte), Integer), CType(CType(224, Byte), Integer), CType(CType(224, Byte), Integer))
        Me.IdBox.Location = New System.Drawing.Point(305, 130)
        Me.IdBox.Name = "IdBox"
        Me.IdBox.Size = New System.Drawing.Size(319, 31)
        Me.IdBox.TabIndex = 1
        '
        'PasswordLabel
        '
        Me.PasswordLabel.AutoSize = True
        Me.PasswordLabel.BackColor = System.Drawing.SystemColors.ControlLight
        Me.PasswordLabel.Font = New System.Drawing.Font("Times New Roman", 12.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
        Me.PasswordLabel.Location = New System.Drawing.Point(156, 206)
        Me.PasswordLabel.Name = "PasswordLabel"
        Me.PasswordLabel.Size = New System.Drawing.Size(110, 26)
        Me.PasswordLabel.TabIndex = 2
        Me.PasswordLabel.Text = "Password"
        '
        'PasswordBox
        '
        Me.PasswordBox.BackColor = System.Drawing.Color.FromArgb(CType(CType(224, Byte), Integer), CType(CType(224, Byte), Integer), CType(CType(224, Byte), Integer))
        Me.PasswordBox.Location = New System.Drawing.Point(305, 204)
        Me.PasswordBox.Name = "PasswordBox"
        Me.PasswordBox.Size = New System.Drawing.Size(319, 31)
        Me.PasswordBox.TabIndex = 3
        '
        'RobotCheck
        '
        Me.RobotCheck.AutoSize = True
        Me.RobotCheck.BackColor = System.Drawing.Color.CadetBlue
        Me.RobotCheck.Font = New System.Drawing.Font("Times New Roman", 11.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
        Me.RobotCheck.ForeColor = System.Drawing.SystemColors.ControlLightLight
        Me.RobotCheck.Location = New System.Drawing.Point(305, 281)
        Me.RobotCheck.Name = "RobotCheck"
        Me.RobotCheck.Size = New System.Drawing.Size(197, 29)
        Me.RobotCheck.TabIndex = 4
        Me.RobotCheck.Text = "I am not a Robot"
        Me.RobotCheck.UseVisualStyleBackColor = False
        '
        'SubmitButton
        '
        Me.SubmitButton.BackColor = System.Drawing.Color.DarkTurquoise
        Me.SubmitButton.Font = New System.Drawing.Font("Times New Roman", 11.0!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Underline), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point)
        Me.SubmitButton.Location = New System.Drawing.Point(476, 369)
        Me.SubmitButton.Name = "SubmitButton"
        Me.SubmitButton.Size = New System.Drawing.Size(217, 50)
        Me.SubmitButton.TabIndex = 5
        Me.SubmitButton.Text = "Submit"
        Me.SubmitButton.UseVisualStyleBackColor = False
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(10.0!, 25.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.BackgroundImage = CType(resources.GetObject("$this.BackgroundImage"), System.Drawing.Image)
        Me.ClientSize = New System.Drawing.Size(800, 450)
        Me.Controls.Add(Me.SubmitButton)
        Me.Controls.Add(Me.RobotCheck)
        Me.Controls.Add(Me.PasswordBox)
        Me.Controls.Add(Me.PasswordLabel)
        Me.Controls.Add(Me.IdBox)
        Me.Controls.Add(Me.IDLabel)
        Me.Name = "Form1"
        Me.Text = "Login Page"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents IDLabel As Label
    Friend WithEvents IdBox As TextBox
    Friend WithEvents PasswordLabel As Label
    Friend WithEvents PasswordBox As TextBox
    Friend WithEvents RobotCheck As CheckBox
    Friend WithEvents SubmitButton As Button
End Class
